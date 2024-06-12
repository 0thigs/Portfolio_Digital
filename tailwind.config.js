/** @type {import('tailwindcss').Config} */

module.exports = {
	content: [
		"./api/templates/**/*.{html,js}",
		"./api/static/**/*.{html,js}",
		"./node_modules/flowbite/**/*.{html,js}",
	],
	theme: {
		extend: {
			
			},
			},
		plugins: [
			require('@midudev/tailwind-animations'),
		],
};
