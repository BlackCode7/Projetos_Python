import axios from 'axios';

const api = axios.create({
    baseUrl: 'http://127.0.0.1:5000/blogs',
}) 

export default api;