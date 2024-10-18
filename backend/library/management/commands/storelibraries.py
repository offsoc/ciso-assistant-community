from pathlib import Path

import structlog, signal
from ciso_assistant.settings import LIBRARIES_PATH
from core.models import StoredLibrary, LoadedLibrary
from django.core.management.base import BaseCommand

logger = structlog.getLogger(__name__)

signal.signal(signal.SIGINT, signal.SIG_DFL)


class Command(BaseCommand):
    help = "Store libraries in the database"

    def add_arguments(self, parser) -> None:
        parser.add_argument("--path", type=str, help="Path to library files")

    def handle(self, *args, **options):
        StoredLibrary.__init_class__()
        path = Path(options.get("path") or LIBRARIES_PATH)
        if path.is_dir():
            library_files = [
                f for f in path.iterdir() if f.is_file and f.suffix == ".yaml"
            ]
        else:
            library_files = [path]
        for fname in library_files:
            # logger.info("Begin library file storage", filename=fname)
            try:
                library = StoredLibrary.store_library_file(fname, True)
                if library:
                    logger.info(
                        "Successfully stored library",
                        filename=fname,
                        library=library,
                    )
            except:
                logger.error("Invalid library file", filename=fname)
        # check consistency of is_loaded
        loaded_library_urns = set([k.urn for k in LoadedLibrary.objects.all()])
        for lib in StoredLibrary.objects.all():
            if lib.urn in loaded_library_urns and not lib.is_loaded:
                print("Fixing (set) is_loaded for", lib.urn)
                lib.is_loaded = True
                lib.save()
            elif lib.urn not in loaded_library_urns and lib.is_loaded:
                print("Fixing (reset) is_loaded for", lib.urn)
                lib.is_loaded = False
                lib.save()
            print(lib.is_loaded, lib.urn)
