import React from 'react'

const LandingPage = () => {
    return (
        <>
            <div className='hero min-h-screen bg-base-200'>
                <div className='hero-content text-center animate-fade-in'>
                    <div className="max-w-md">
                        <h1 className='text-5xl font-bold'>Welcome to my App</h1>
                        <p className="py-6">Practice authentication with Django and React, and get familiar with styling using DaisyUI.</p>
                        <a href="/signup" className='btn btn-primary'>Get Started</a>
                    </div>
                </div>
            </div>
            <div className='py-10 bg-base-100'>
                <h2 className='text-3xl font-bold text-center'>Features</h2>
                <div className='flex flex-wrap justify-center mt-6'>
                    <div className='card w-96 bg-base-200 shadow-xl m-4'>
                        <div className='card-body'>
                            <h2 className='card-title'>Authentication</h2>
                            <p>Practice authentication with Django and React.</p>
                        </div>
                    </div>
                    <div className='card w-96 bg-base-200 shadow-xl m-4'>
                        <div className='card-body'>
                            <h2 className='card-title'>Styling</h2>
                            <p>Get familiar with styling using DaisyUI.</p>
                        </div>
                    </div>
                    <div className='card w-96 bg-base-200 shadow-xl m-4'>
                        <div className='card-body'>
                            <h2 className='card-title'>Responsive</h2>
                            <p>Build a responsive application.</p>
                        </div>
                    </div>
                </div>
            </div>
            <footer className="footer p-10 bg-base-200 text-base-content">
                <div>
                    <span className="footer-title">Company</span>
                    <a className="link link-hover">About us</a>
                    <a className="link link-hover">Contact</a>
                    <a className="link link-hover">Jobs</a>
                </div>
                <div>
                    <span className="footer-title">Legal</span>
                    <a className="link link-hover">Terms of use</a>
                    <a className="link link-hover">Privacy policy</a>
                    <a className="link link-hover">Cookie policy</a>
                </div>
            </footer>
        </>
    )
}

export default LandingPage
