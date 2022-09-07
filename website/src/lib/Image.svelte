<script lang="ts">
  export let largestBorder = 512;
  export let src: string;
  export let alt: string;
  export let loading = "eager";
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
  class:hidden={!loaded}
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
    opacity: 1;
    transition: opacity 1s;
  }
  .hidden {
    opacity: 0;
  }
</style>
