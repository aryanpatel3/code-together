import { Box, Container, Stack, Text } from "@chakra-ui/react";

export function LeftSide(props) {
  const { title, description } = props.data;

  return (
    <Box w="35%" borderRight="1px" borderColor="gray.200">
      <Container py={4}>
        <Stack spacing={3}>
          <Text fontSize="xl" fontWeight="bold">
            {title}
          </Text>
          <Text>{description}</Text>
        </Stack>
      </Container>
    </Box>
  );
}
