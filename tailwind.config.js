/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{jinja, js, css}"],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
    require('flowbite/plugin'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/container-queries'),
  ],
}

