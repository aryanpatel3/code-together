import CodeMirror from "@uiw/react-codemirror";
import { python } from "@codemirror/lang-python";
import { EditorView } from "@codemirror/view";
import { useColorMode } from "@chakra-ui/react";

export function Editor({ code, onCodeChange }) {
  const { colorMode } = useColorMode();

  const fixedHeightEditor = EditorView.theme({
    "&": { height: "500px" },
    ".cm-scroller": { overflow: "auto" },
  });

  return (
    <CodeMirror
      width={"100%"}
      value={code}
      extensions={[python(), fixedHeightEditor]}
      onChange={onCodeChange}
      theme={colorMode}
    />
  );
}
