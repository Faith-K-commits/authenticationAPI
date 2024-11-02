import App from "./App";
import LandingPage from "./components/LandingPage";
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
        ],
    }
]

export default routes;