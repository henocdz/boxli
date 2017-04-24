import 'whatwg-fetch';
import { retrieveToken, isAuthenticated } from './auth'
/**
 * Parses the JSON returned by a network request
 *
 * @param  {object} response A response from a network request
 *
 * @return {object}          The parsed JSON from the request
 */
function parseJSON(response) {
  return response.json();
}

/**
 * Checks if a network request came back fine, and throws an error if not
 *
 * @param  {object} response   A response from a network request
 *
 * @return {object|undefined} Returns either the response, or throws an error
 */
function checkStatus(response) {
  if (response.status >= 200 && response.status < 300) {
    return response;
  }

  const error = new Error(response.statusText);
  error.response = response;
  throw error;
}

/**
 * Requests a URL, returning a promise
 *
 * @param  {string} url       The URL we want to request
 * @param  {object} [options] The options we want to pass to "fetch"
 *
 * @return {object}           The response data
 */
export default function request(url, options = {}) {
  const data = { ...options }
  let headers = 'headers' in options ? options.headers : {}
  headers = {
    'Content-Type': 'application/json',
    ...headers
  }

  if(isAuthenticated()){
    headers.Authorization = 'Token ' + retrieveToken()
  }
  data.headers = headers

  if (data.body) {
    data.body = JSON.stringify(data.body)
  }

  return fetch(url, data)
    .then(checkStatus)
    .then(parseJSON)
}
