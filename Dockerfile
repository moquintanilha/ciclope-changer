ARG CHATOPS_HOST 
FROM node:16
WORKDIR /app
ENV CHATOPS_HOST=$CHATOPS_HOST
COPY package.json ./
RUN npm install
COPY . .
ENTRYPOINT [ "npm", "start" ]