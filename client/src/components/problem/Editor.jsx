import CodeMirror from "@uiw/react-codemirror";
import { python } from "@codemirror/lang-python";
import { EditorView } from "@codemirror/view";

export function Editor(props) {
  const { code, onCodeChange } = props;

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
      theme={"dark"}
    />
  );
}
