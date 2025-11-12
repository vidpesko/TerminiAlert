module.exports = {
  apps : [
    {
      name: "TerminiAlert-Frontend",
      script: 'build/index.js',
      watch: '.',
      env: {
        HTTPS_ENABLED: "false",
        DOMAIN: "termini.pesko.si",
        PORT: "3003",
        HOST: "127.0.0.1",
        ORIGIN: "https://termini.pesko.si"
      }
    }
  ],
};
