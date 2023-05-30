#!/usr/bin/node
const request = require('request');
const URL_API = 'https://swapi-api.alx-tools.com/api/';

if (process.argv.length > 2) {
  request(`${URL_API}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const URLCharacters = JSON.parse(body).characters;
    const NameCharacters = URLCharacters.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, (promiseError, __, charactersReqBody) => {
            if (promiseError) {
              reject(promiseError);
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        })
    );

    Promise.all(NameCharacters)
      .then((names) => console.log(names.join('\n')))
      .catch((allErr) => console.log(allErr));
  });
}
