<script lang="ts">
	// Most of your app wide CSS should be put in this file
	import '../../app.postcss';
	import { AppShell, AppBar, LightSwitch } from '@skeletonlabs/skeleton';
	import { safeTranslate } from '$lib/utils/i18n';

	import SideBar from '$lib/components/SideBar/SideBar.svelte';
	import Breadcrumbs from '$lib/components/Breadcrumbs/Breadcrumbs.svelte';
	import { pageTitle, clientSideToast, selectedTheme } from '$lib/utils/stores';
	import { getCookie, deleteCookie } from '$lib/utils/cookies';
	import { browser } from '$app/environment';
	import * as m from '$paraglide/messages';

	import CommandPalette from '$lib/components/CommandPalette/CommandPalette.svelte';

	let sidebarOpen = true;

	$: classesSidebarOpen = (open: boolean) => (open ? 'ml-7 lg:ml-64' : 'ml-7');

	$: if (browser) {
		const fromLogin = getCookie('from_login');
		if (fromLogin === 'true') {
			deleteCookie('from_login');
			fetch('/fe-api/waiting-risk-acceptances').then(async (res) => {
				const data = await res.json();
				const number = data.count ?? 0;
				if (number <= 0) return;
				clientSideToast.set({
					message: m.waitingRiskAcceptances({
						number: number,
						s: number > 1 ? 's' : '',
						itPlural: number > 1 ? 'i' : 'e'
					}),
					type: 'info'
				});
			});
		}
	}

	const themes = [
		'ciso-theme',
		'skeleton',
		'modern',
		'crimson',
		'seafoam',
		'vintage',
		'hamlindigo',
		'wintry'
	];

	let value = 'ciso-theme';

	$: $selectedTheme = value;
</script>

<!-- App Shell -->
<AppShell
	slotPageContent="p-8 bg-gradient-to-br from-primary-100 to-surface-200 dark:from-primary-900 dark:to-tertiary-800"
	regionPage="transition-all duration-300 {classesSidebarOpen(sidebarOpen)}"
>
	<svelte:fragment slot="sidebarLeft">
		<SideBar bind:open={sidebarOpen} />
	</svelte:fragment>
	<svelte:fragment slot="pageHeader">
		<AppBar background="bg-surface-50-900-token" padding="py-2 px-4">
			<LightSwitch />
			<select bind:value>
				{#each themes as theme}
					<option value={theme} selected={theme === 'ciso-theme'}>{theme}</option>
				{/each}
			</select>
			<h3
				class="h3 font-bold pb-1 bg-gradient-to-r from-pink-500 to-violet-600 bg-clip-text text-transparent"
				id="page-title"
			>
				{safeTranslate($pageTitle)}
			</h3>
			<hr class="w-screen my-1" />
			<Breadcrumbs />
		</AppBar>
	</svelte:fragment>
	<!-- Router Slot -->
	<CommandPalette />
	<slot />
	<!-- ---- / ---- -->
</AppShell>
