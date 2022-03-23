import {writable} from "svelte/store"

let theme = writable("light");

export {theme};
