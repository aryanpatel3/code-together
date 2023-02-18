import { Container, Textarea } from "@nextui-org/react";

export function Editor() {
  return (
    <Container>
      <Textarea
        width="100%"
        label="Write code here:"
        placeholder="Start typing..."
      />
    </Container>
  );
}
