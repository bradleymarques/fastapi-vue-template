FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@4.5.13 -g

COPY package.json .
COPY package-lock.json .
RUN npm install

RUN mkdir -p node_modules/.cache
RUN chmod -R 777 node_modules/.cache

CMD ["npm", "run", "serve"]
