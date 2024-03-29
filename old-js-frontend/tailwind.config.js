/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    colors: {
      transparent: 'transparent',
      white: '#FDFDFD',
      black: '#000000',
      background: '#F5F5F5',
      darkGray: '#505050',
      lightGray: '#A6ACAC',
      veryLightYellow: '#fff6be',
      lightYellow: '#ffeda3',
      medYellow: '#FFE486',
      orange: '#f6c510',
      darkGreen: '#223F41',
      lightGreen: '#E5FBF5',
      green: '#05CD99',
      lightRed: '#FDEEED',
      red: '#EE5D50',
    },
    borderRadius: {
      '2xs': '4px',
      xs: '8px',
      sm: '12px',
      md: '16px',
      lg: '20px',
      xl: '24px',
      '2xl': '28px',
      '3xl': '32px',
      '4xl': '36px',
      '5xl': '40px',
      '6xl': '44px',
      '7xl': '48px',
      full: '9999px',
    },
    fontSize: {
      xs: '12px',
      sm: '14px',
      md: '16px',
      lg: '18px',
      xl: '20px',
      '2xl': '24px',
      '3xl': '28px',
      '4xl': '32px',
      '5xl': '36px',
      '6xl': '40px',
      '7xl': '44px',
      '8xl': '48px',
      '9xl': '52px',
      '10xl': '56px',
      '11xl': '60px',
      '12xl': '64px',
    },
    screens: {
      '3xs': '300px',
      '2xs': '360px',
      xs: '480px',
      sm: '640px',
      md: '768px',
      lg: '840px',
      xl: '1024px',
      '2xl': '1280px',
      '3xl': '1400px',
      '4xl': '1600px',
      '5xl': '1800px',
    },
    extend: {
      margin: {
        0.25: '1px',
        4.5: '18px',
      },
      padding: {
        4.5: '18px',
      },
      width: {
        3.5: '14px',
        4.5: '18px',
      },
    },
  },
  plugins: [],
};
