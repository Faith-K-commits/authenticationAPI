import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/login/', {
                email,
                password,
            });
            console.log(response.data);
            localStorage.setItem('token', response.data.accessToken);
            navigate('/home');
        } catch (error) {
            console.error('There was an error logging in!', error);
            alert('Login failed');
        }
    };

    return (
        <div className="flex justify-center items-center h-screen bg-base-200">
            <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow-md w-80">
                <h2 className="text-2xl mb-4">Login</h2>
                <div className="mb-4">
                    <label className="block mb-1">Email</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        className="input input-bordered w-full"
                        required
                    />
                </div>
                <div className="mb-4">
                    <label className="block mb-1">Password</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="input input-bordered w-full"
                        required
                    />
                </div>
                <button type="submit" className="btn btn-primary w-full">Login</button>
            </form>
        </div>
    );
};

export default Login;