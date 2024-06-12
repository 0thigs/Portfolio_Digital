/** @type {import('tailwindcss').Config} */

module.exports = {
	content: [
		"./api/templates/**/*.{html,js}",
		"./api/static/**/*.{html,js}",
		"./node_modules/flowbite/**/*.{html,js}",
	],
	theme: {
		extend: {
			fontFamily: {
				montserrat: ["Montserrat", "sans-serif"],
			},
			colors: {
				defaultPurple: "#4A1D96",
				strokePurple: "#AC94FA",
			},
			animation: {
				"infinite-scroll": "infinite-scroll 35s linear infinite",
				"": "infinite-scroll 35s linear infinite",
			},
			keyframes: {
				"infinite-scroll": {
					from: { transform: "translateX(0)" },
					to: { transform: "translateX(-100%)" },
				},
			},
			},
			},
		plugins: [
			require('@midudev/tailwind-animations'),
		],
};
