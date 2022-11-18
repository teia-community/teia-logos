<div class="container">
  <h1>Press Kit</h1>
  <div class="box">
    <h2>"Classic" Logos</h2>

    <p class="summary">
      If you would like to use teia logo, please use one from the following
      archive
    </p>
    <a
      class="download"
      target="_blank"
      rel="noreferrer"
      href="https://github.com/teia-community/teia-logos/raw/main/dist/classic.zip"
      >Download (svg + png)</a
    >
    <!-- <img src={pfp} width="120px" alt="teia pfp" /> -->
  </div>
  <div class="box">
    <h2>Font</h2>
    <p class="summary">
      Teia use the
      <a rel="noreferrer" target="_blank" href="https://typeof.net/Iosevka"
        >Ioveska Extended</a
      > font across the entire site.
    </p>
  </div>
</div>

<style>
  .box {
    border: 1px solid var(--text-color);
    padding: 1.5em 3em;
    margin: 1em;
    text-align: center;
  }
  .summary {
    text-align: justify;
    width: 340px;
  }
  h1 {
    font-family: "iosevka-extended";
  }
  h2 {
    font-weight: 600;
  }
  .download {
    margin: 1em;
    padding: 1em;
    pointer-events: all;
    border-radius: 0px;
    cursor: pointer;
    font-size: 12px;
    font-weight: 400;
    background: var(--text-color);
    color: var(--bg-color);
  }

  .container {
    display: flex;
    width: 85%;
    margin-left: auto;
    margin-right: auto;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    flex-direction: column;
  }
</style>
