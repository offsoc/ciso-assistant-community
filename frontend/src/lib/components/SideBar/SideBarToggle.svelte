<script lang="ts">
	export let open: boolean;

	function toggle() {
		open = !open;
	}

	$: classesSidebarOpenButton = (open: boolean) => (open ? 'left-[15.3rem]' : 'rotate-180 left-5');
</script>

<!-- SIDEBAR TOGGLE -->
<button
	on:click={toggle}
	class="{classesSidebarOpenButton(
		open
	)} z-20 fixed w-6 h-6 rounded-full content-center self-center bg-surface-50-900-token shadow border text-surface-600-300-token hover:scale-105 hover:bg-primary-700-200-token hover:text-surface-50-900-token transition-all duration-300 top-1/2 bottom-1/2"
	data-testid="sidebar-toggle-btn"
>
	<i class="fa-solid fa-angle-left" />
</button>
