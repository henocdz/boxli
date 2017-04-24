const env = {
  API_BASE_URL: process.env.NODE_ENV === 'production' ? 'http://api.boxli.co' : 'http://localhost:8000',
  API_URL: process.env.NODE_ENV === 'production' ? 'http://api.boxli.co/api' : 'http://localhost:8000/api',
  CREATE_LINK_URL: '/links/'
}


export default env
