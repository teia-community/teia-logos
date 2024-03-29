import { sveltekit } from "@sveltejs/kit/vite";
import svg from "@poppanator/sveltekit-svg";
import child_process from "child_process";
import { fileURLToPath } from "url";
import { readFileSync } from "fs";

const file = fileURLToPath(new URL("package.json", import.meta.url));
const json = readFileSync(file, "utf8");
const packageJSON = JSON.parse(json);

const config = {
  plugins: [sveltekit(), svg()],
  server: {
    port: 3099,
    fs: {
      // Allow serving files from one level up to the project root
      allow: ["../.."],
    },
  },

  define: {
    __package_json__: packageJSON,
  },
};

export default config;
