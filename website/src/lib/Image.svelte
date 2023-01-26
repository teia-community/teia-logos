<script lang="ts">
  export let largestBorder = 512;
  export let src: string;
  export let alt: string;
  export let loading = "eager";
  export let bordered = false;
  let width: number;
  let height: number;
  let loaded = false;

  let size = {
    width: 0,
    height: 0,
  };

  const onImgLoad = (
    event: Event & { currentTarget: EventTarget & HTMLImageElement }
  ) => {
    size = {
      width: event.currentTarget.naturalWidth,
      height: event.currentTarget.naturalHeight,
    };
    if (size.width > size.height) {
      width = largestBorder;
      height = (size.height / size.width) * largestBorder;
    } else {
      width = (size.width / size.height) * largestBorder;
      height = largestBorder;
    }
    loaded = true;
  };
</script>

<img
  class:loaded
  class:bordered
  on:click
  on:load={onImgLoad}
  {height}
  {width}
  {loading}
  {src}
  {alt}
/>

<!-- <p>{size.height}x{size.width} {largestBorder}</p> -->
<style>
  img {
    min-width: 32px;
    min-height: 32px;
    opacity: 0;
    /* transition: opacity 0.2s; */
  }
  .bordered {
    border: 1px var(--text-color) solid;
  }
  .loaded {
    opacity: 1;
  }
</style>
