<script context="module">
  export const prerender = true;
</script>

<script>
  import LogoViewer from "$lib/LogoViewer.svelte";
  import { raw_url } from "$lib/constants";
</script>

<LogoViewer root="pride" fetch_url={`${raw_url}/logos_pride.json`} />
