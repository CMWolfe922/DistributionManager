import { useEffect, useState } from "react"
import { deleteorder, getorder } from "../services/ApiService"
import AddOrder from "./AddOrder"

const OrderList = () => {
    const [orders, setOrders] = useState([])
    const [showAddOrder, setShowAddOrder] = useState(false)

    useEffect(() => {
        let mount = true
        getorder()
            .then(res => {
                console.log("Response from order api ", res)
                setOrders(res)
                return() => mount = false
            })
    }, [])

    const handleDeleteBtn = (id) => {
        deleteorder(id)
            .then(() => setOrders(orders.filter(p => p.order_id !== id)))
    }

    const handleCancelBtn = () => {
        setShowAddOrder(false);
        getorder()
            .then(res => {
                console.log("Response from API ", res)
                setOrders(res)
            })
    }

    return (
        <div className="container">
           <h3>Order List</h3>
            <table className="table table-striped table-hover table-bordered">
                <thead className="table-dark">
                    <tr>
                        <th scope="col">First Name</th>
                        <th scope="col">Last Name</th>
                        <th scope="col">Order Type</th>
                        <th scope="col">Order ID</th>
                        <th scope="col">Order Action</th>
                    </tr>
                </thead>
                <tbody>
                    {orders.map(order => 
                        <tr key={order.order_id}>
                            <td>{order.first_name}</td>
                            <td>{order.last_name}</td>
                            <td>{order.order_type}</td>
                            <td>{order.order_id}</td>
                            <td>
                                {/* <button className="btn btn-primary m-2" onClick={()=>{}}>Edit</button> */}
                                <button className="btn btn-danger" onClick={() => handleDeleteBtn(order.order_id)}>Delete</button>
                            </td>
                        </tr>
                    )}
                </tbody>
           </table>
           <br />
           <button className="btn btn-success" onClick={()=>setShowAddOrder(!showAddOrder)}>Create New Order</button>
           <br />
           <br />
           {showAddOrder && <AddOrder handleCancelBtn={handleCancelBtn} />}
        </div>
    )
}

export default OrderList