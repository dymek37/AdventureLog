import { fail, redirect } from '@sveltejs/kit';

import type { Actions, PageServerLoad } from './$types';
import type { User } from '$lib/types';
const PUBLIC_SERVER_URL = process.env['PUBLIC_SERVER_URL'];
const serverEndpoint = PUBLIC_SERVER_URL || 'http://localhost:8000';

export const load: PageServerLoad = async (event) => {
	if (!event.locals.user) {
		return redirect(302, '/');
	} else {
		let users: User[] = [];
		let usersFetch = await event.fetch(`${serverEndpoint}/auth/public-profiles/`, {
			headers: {
				Cookie: `${event.cookies.get('auth')}`
			}
		});
		if (!usersFetch.ok) {
			console.error('Failed to fetch users');
			return fail(500, {
				message: 'Failed to fetch users'
			});
		} else {
			let usersJson = await usersFetch.json();
			users = usersJson;
		}
		return {
			props: {
				users
			}
		};
	}
};
