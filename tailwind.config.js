/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{jinja, js, css}"],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
    require('flowbite/plugin'),
  ],
}

