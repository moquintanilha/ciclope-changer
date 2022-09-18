ARG CHATOPS_HOST 
FROM node:16
WORKDIR /app
ENV CHATOPS_HOST=$CHATOPS_HOST
COPY package.json ./
RUN npm install
COPY app/  ./app/
COPY package.js .
COPY index.spec.js .
COPY jest.config.js .
COPY index.js .
ENTRYPOINT [ "npm", "start" ]