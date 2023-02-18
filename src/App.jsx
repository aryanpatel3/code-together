import "./App.css";
import { NextUIProvider } from "@nextui-org/react";

import { Editor } from "./components/Editor";

function App() {
  return (
    <NextUIProvider>
      <Editor />
    </NextUIProvider>
  );
}

export default App;
