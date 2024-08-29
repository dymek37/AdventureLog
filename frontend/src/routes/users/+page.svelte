<script lang="ts">
	import type { User } from '$lib/types.js';
	import { onMount } from 'svelte';

	export let data;
	let users: User[];
	console.log(data);

	if (data && data.props) {
		users = data.props?.users;
	}
</script>

{#each users as user}
	<div>
		<h2>{user.first_name}</h2>
		<p>{user.last_name}</p>
		<p>{user.username}</p>
	</div>
{/each}
