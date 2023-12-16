import axios from "axios";

export function getorder() {
    return axios.get('http://127.0.0.1:8000/order/')
        .then(res => res.data)
}

export function deleteorder(id) {
    return axios.delete('http://127.0.0.1:8000/order/' + id + '/')
        .then(res => res.data)
}