import adapterAuto from '@sveltejs/adapter-auto';
import autoPreprocess from 'svelte-preprocess';
import adapterStatic from '@sveltejs/adapter-static';

const ghPages = process.env.GITHUB_ACTIONS === 'true'

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: autoPreprocess(),
	kit: {
		adapter: ghPages ? adapterStatic() :  adapterAuto(),
		paths: {
      // assets: ghPages ? 'https://raw.githubusercontent.com/teia-community/teia-logos/gh-pages': '',
      base: ghPages ? '/teia-logos' : '',
    },
	}

};

export default config;
