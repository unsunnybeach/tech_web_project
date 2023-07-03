import { useState, useEffect } from "react";

import { MainNav } from "@/components/MainNav";
import { UserNav } from "../CustomersPage/components/UserNav";
import { navigationLinks } from "@/config/navigationLinks";

export const OrdersPage = () => {
    const [ordersData, setOrdersData] = useState([]);

    const fetchOrdersData = async () => {
        const response = await fetch("http://127.0.0.1:8000/orders");
        const data = await response.json();
        setOrdersData(data);
    };

    useEffect(() => {
        fetchOrdersData();
    }, []);

    console.log(ordersData)
    console.log("hi")

    return (
        <div className="hidden flex-col md:flex">
            <div className="border-b">
                <div className="flex h-16 items-center px-4">
                    <MainNav className="mx-6" links={navigationLinks} />
                    <div className="ml-auto flex items-center space-x-4">
                        <UserNav />
                    </div>
                </div>
            </div>
        <div className="flex-1 space-y-4 p-8 pt-6">
            <div className="flex items-center justify-between space-y-2">
                <h2 className="text-3xl font-bold tracking-tight">Orders</h2>
            </div>
        <div className="hidden h-full flex-1 flex-col space-y-8 md:flex">
        <ul className="allOrders">
            {ordersData.map((item) => (
                <li key={item.id}>
                    <p>
                        <strong>Customer ID: </strong>
                        {item.customer_id}
                    </p>
                    <p>
                        <strong>Ordered items: </strong>
                        {item.ordered_items.join(", ")}
                    </p>
                    
                </li>
            ))}
        </ul>
        </div>
        </div>
        </div>
    );
};
