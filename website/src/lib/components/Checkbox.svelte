<script>
  export let label = "";
  export let value = false;
</script>

<label class="container"
  >{label}
  <input type="checkbox" bind:checked={value} />
  <span class="checkmark" />
</label>

<style>
  /* The container */
  .container {
    display: block;
    position: relative;
    padding-left: 2em;
    margin-bottom: 0.25em;
    cursor: pointer;
    /* font-size: 22px; */
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }

  /* Hide the browser's default checkbox */
  .container input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
    height: 0;
    width: 0;
  }

  /* Create a custom checkbox */
  .checkmark {
    position: absolute;
    top: 0;
    left: 0;
    height: 1.25em;
    width: 1.25em;
    background-color: var(--bg-color);
    border: 1px solid var(--text-color);
  }

  /* On mouse-over, add a grey background color */
  .container:hover input ~ .checkmark {
    background-color: #ccc;
  }

  /* When the checkbox is checked, add a background */
  .container input:checked ~ .checkmark {
    background-color: var(--bg-color);
  }

  /* Create the checkmark/indicator (hidden when not checked) */
  .checkmark:after {
    content: "";
    position: absolute;
    display: none;
  }

  /* Show the checkmark when checked */
  .container input:checked ~ .checkmark:after {
    display: block;
  }

  /* Style the checkmark/indicator */
  .container .checkmark:after {
    left: 0.33em;
    top: 0.2em;
    width: 5px;
    height: 0.5em;
    border: solid var(--text-color);
    border-width: 0 3px 3px 0;
    -webkit-transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    transform: rotate(45deg);
  }
</style>
