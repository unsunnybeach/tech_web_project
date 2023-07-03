import { MainNav } from "@/components/MainNav";
import { navigationLinks } from "../config/navigationLinks";
import { UserNav } from "./CustomersPage/components/UserNav";
import { useState } from "react";

export const AddCustomerPage = () => {

  const [firstName, setFirstName] = useState("");
  const [surname, setSurname] = useState("");
  const [email, setEmail] = useState("");
  const [number, setNumber] = useState("");

  const getFirstName = (event) => {
    setFirstName(event.target.value);
  };

  const getSurname = (event) => {
    setSurname(event.target.value);
  };

  const getEmail = (event) => {
    setEmail(event.target.value);
  };
  const getNumber = (event) => {
    setNumber(event.target.value);
  };

  const submitedFormHandler = async (e) => {
    e.preventDefault();

    const customerData = {
      name: firstName,
      surname: surname,
      email: email,
      phone_number: number
    };

    const response = fetch("http://127.0.0.1:8000/customers", {
      method: "POST",
      body: JSON.stringify(customerData),
      headers: {
        "Content-Type": "application/json",
      },
    });
    console.log(response);


    setFirstName("");
    setSurname("");
    setEmail("");
    setNumber("");
  };



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
          <h2 className="text-3xl font-bold tracking-tight">Add customer</h2>
        </div>
        <div className="hidden h-full flex-1 flex-col space-y-8 md:flex"></div>
      </div>
      <form onSubmit={submitedFormHandler} className="addCustomer">
        <strong>First name</strong>
        <input onChange={getFirstName}
        value={firstName}
        placeholder="Your Name"
        type="text"
        ></input>
        
        <strong>Surname</strong>
        <input onChange={getSurname}
        value={surname}
        placeholder="Your Surname"
        type="text"
        ></input>
        
        <strong>Email</strong>
        <input onChange={getEmail}
        value={email}
        placeholder="abc@mail.com"
        type="text"
        ></input>
        
        <strong>Phone number</strong>
        <input onChange={getNumber}
        value={number}
        placeholder="000-000-000"
        type="text"
        ></input>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

