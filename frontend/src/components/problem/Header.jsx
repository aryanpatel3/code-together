import {
  Box,
  Flex,
  IconButton,
  Spacer,
  Text,
  useColorMode,
} from "@chakra-ui/react";
import { MoonIcon, SunIcon } from "@chakra-ui/icons";

export function Header() {
  const { colorMode, toggleColorMode } = useColorMode();
  return (
    <Box h="50px">
      <Flex
        alignItems="center"
        justifyContent="center"
        h="100%"
        borderBottom="1px"
        borderColor="gray.200"
      >
        <Text fontWeight="bold" fontSize="lg" ml="4">
          Code Together
        </Text>
        <Spacer />
        <IconButton
          m={2}
          justifySelf={"flex-end"}
          aria-label="Toggle dark mode"
          icon={colorMode === "light" ? <SunIcon /> : <MoonIcon />}
          onClick={toggleColorMode}
        />
      </Flex>
    </Box>
  );
}
