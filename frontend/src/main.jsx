import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from "react-router";
import './index.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import Register from "./components/Register"
import ListUsers from './components/ListUsers';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Register />} />
        <Route path="/list" element={<ListUsers />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
