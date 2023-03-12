import { useCallback, useState } from "react";
import CodeMirror from "@uiw/react-codemirror";
import { python } from "@codemirror/lang-python";
import { Button, Container, Spacer } from "@chakra-ui/react";
import axios from "axios";

export function Editor() {
  const [code, setCode] = useState(`print("Hello World!")`);
  const [results, setResults] = useState([]);

  const onCodeChange = useCallback((value) => {
    console.log("value:", value);
    setCode(value);
  }, []);

  const handleRunClick = async () => {
    const res = await axios.post("http://localhost:8000/code", { code: code });
    setResults(res.data.results);
    console.log(results);
  };

  return (
    <Container>
      <Button auto onPress={handleRunClick}>
        Run
      </Button>
      <Spacer />
      <CodeMirror
        width={"100%"}
        value={code}
        height="30em"
        extensions={[python()]}
        onChange={onCodeChange}
        theme={"dark"}
      />
      Result:
      <Container>
        <ul>
          {results.map((artist, i) => (
            <li key={i}>{artist.toString()}</li>
          ))}
        </ul>
      </Container>
    </Container>
  );
}
