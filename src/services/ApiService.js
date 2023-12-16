import axios from "axios";

export function getorder() {
    return axios.get('http://127.0.0.1:8000/order/')
        .then(res => res.data)
}