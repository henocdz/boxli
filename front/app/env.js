const env = {
  API_BASE_URL: process.env.NODE_ENV === 'production' ? 'https://boxli-api.herokuapp.com' : 'http://localhost:8000',
  API_URL: process.env.NODE_ENV === 'production' ? 'https://boxli-api.herokuapp.com/api' : 'http://localhost:8000/api',
  CREATE_LINK_URL: '/links/'
}


export default env
