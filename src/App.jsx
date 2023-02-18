import "./App.css";

import { Editor } from "./components/Editor";

import { NextUIProvider } from "@nextui-org/react";

function App() {
  return (
    <NextUIProvider>
      <Editor />
    </NextUIProvider>
  );
}

export default App;
