import { useCallback } from "react";
import CodeMirror from "@uiw/react-codemirror";
import { python } from "@codemirror/lang-python";
import { Button, Spacer, Container } from "@nextui-org/react";

export function Editor() {
  const onChange = useCallback((value) => {
    console.log("value:", value);
  }, []);

  const handleRunClick = () => {
    console.log("run code!");
  };

  return (
    <Container
      css={{
        py: "2em",
      }}
    >
      <Button auto onPress={handleRunClick}>
        Run
      </Button>
      <Spacer />
      <CodeMirror
        value="print('hello world!')"
        height="30em"
        extensions={[python()]}
        onChange={onChange}
      />
    </Container>
  );
}
