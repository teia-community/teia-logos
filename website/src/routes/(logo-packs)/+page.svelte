<script context="module">
  export const prerender = true;
</script>

<script>
  import LogoViewer from "$lib/LogoViewer.svelte";
  import { raw_url } from "$lib/constants";
</script>

<LogoViewer
  label="Logos Rotation"
  theme_based
  fetch_url={`${raw_url}/logos.json`}
/>
