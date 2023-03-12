import React from "react";
import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import { ChakraProvider } from "@chakra-ui/react";
import chakraTheme from "@chakra-ui/theme";
import { Problem } from "./components/Problem";

function App() {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <>
        <Route path="/" element={<div>This is the home page!</div>} />
        <Route path="problems/1" element={<Problem />} />
      </>
    )
  );
  return (
    <ChakraProvider theme={chakraTheme}>
      <RouterProvider router={router} />
    </ChakraProvider>
  );
}

export default App;
