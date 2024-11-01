import React from 'react'

const NavBar = () => {
    return (
        <div className='navbar bg-base-100 sticky top-0'>
            <div className='flex-1'>
                <a className='btn btn-ghost normal-case text-xl' href="/">Home</a>
            </div>
            <div className='flex-none'>
                <a className='btn btn-ghost' href="/login">Login</a>
                <a className='btn btn-ghost' href="/signup">Signup</a>
            </div>
        </div>
    )
}

export default NavBar
