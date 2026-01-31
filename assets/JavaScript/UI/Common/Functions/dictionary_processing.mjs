function get(obj, key, defaultValue = null) {
  return obj.hasOwnProperty(key) ? obj[key] : defaultValue;
}

export default get;