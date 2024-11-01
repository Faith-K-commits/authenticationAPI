import React from 'react'

const Hero = () => {
  return (
    <div className='hero min-h-screen bg-base-200'>
      <div className='hero-content text-center animate-fade-in'>
        <div className="max-w-md">
          <h1 className='text-5xl font-bold'>Welcome to my App</h1>
          <p className="py-6">Practice authentication with Django and React, and get familiar with styling using DaisyUI.</p>
          <a href="/signup" className='btn btn-primary'>Get Started</a>
        </div>
      </div>
    </div>
  )
}

export default Hero