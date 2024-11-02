import App from "./App";
import LandingPage from "./components/LandingPage";
import Home from "./Pages/Home";
import Login from "./Pages/Login";


const routes = [
    {
        path: '/',
        element: <App />,
        children: [
            {
                path: '/',
                element: <LandingPage />,
            },
            {
                path: '/login',
                element: <Login />,
            },
            {
                path: '/home',
                element: <Home />,
            },
        ],
    }
]

export default routes;