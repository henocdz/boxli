const TOKEN_KEY = 'wizetoken'

const retrieveToken = () => {
  return localStorage.getItem(TOKEN_KEY) || null
}

const saveToken = (token) => {
  localStorage.setItem(TOKEN_KEY, token)
}

const logout = () => {
  localStorage.removeItem(TOKEN_KEY)
}

const isAuthenticated = () => {
  return !!retrieveToken()
}

export { saveToken, retrieveToken, logout, isAuthenticated }
