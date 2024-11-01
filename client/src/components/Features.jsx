import React from 'react'

const Features = () => {
    return (
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
    )
}

export default Features