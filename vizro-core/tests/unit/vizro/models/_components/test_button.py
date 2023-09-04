"""Unit tests for vizro.models.Button."""
import dash_bootstrap_components as dbc
import pytest

import vizro.models as vm
from vizro.actions import export_data
from vizro.models._action._actions_chain import ActionsChain


class TestButtonInstantiation:
    """Tests model instantiation and the validators run at that time."""

    def test_create_default_button(self):
        button = vm.Button()
        assert hasattr(button, "id")
        assert button.type == "button"
        assert button.text == "Click me!"
        assert button.actions == []

    @pytest.mark.parametrize(
        "text",
        ["Test", 123, 1.23, True, """# Header""", """<p>Hello </p>"""],
    )
    def test_create_button_with_optional(self, text):
        button = vm.Button(text=text)
        assert hasattr(button, "id")
        assert button.type == "button"
        assert button.text == str(text)
        assert button.actions == []

    def test_create_button_with_one_valid_action(self):
        button = vm.Button(actions=[vm.Action(function=export_data())])
        button_actions_chain = button.actions[0]
        assert hasattr(button, "id")
        assert button.type == "button"
        assert button.text == "Click me!"
        assert len(button.actions) == 1
        assert isinstance(button_actions_chain, ActionsChain)
        assert button_actions_chain.trigger.component_property == "n_clicks"


class TestBuildMethod:
    def test_button_build(self):
        button = vm.Button(id="button_id")
        component = button.build()

        assert isinstance(component["button_id"], dbc.Button)
        assert hasattr(component["button_id"], "id")
