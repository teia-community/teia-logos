import adapterAuto from '@sveltejs/adapter-auto';
import autoPreprocess from 'svelte-preprocess';
import adapterStatic from '@sveltejs/adapter-static';

const ghPages = process.env.GITHUB_ACTIONS === 'true'

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: autoPreprocess(),
	kit: {
		adapter: ghPages ? adaptaterStatic() :  adapterAuto(),
	}

};

export default config;
